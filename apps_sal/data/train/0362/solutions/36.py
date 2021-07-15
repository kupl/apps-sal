class Solution:
    # def numberWays(self, hats: List[List[int]]) -> int:
        # const = 10**9+7
        # cache = {}
        # matr = [[False]*len(hats) for i in range(40)]
        # maxx = -1
        # used_h = [False]*40
        # for j in range(len(hats)):
        #     for i in hats[j]:
        #         matr[i-1][j] = True
        #         maxx = max(i-1, maxx)
        #         used_h[i-1] = True
        # def s(mask_p, h, n):
        #     if n > h+1 or h < 0:
        #         return 0
        #     c = str(h)+mask_p
        #     if c in cache:
        #         return cache[c]
        #     res = s(mask_p, h-1, n)
        #     if used_h[h]:
        #         for p in range(len(matr[h])):
        #             if mask_p[p] == \"1\" and matr[h][p]:
        #                 if n > 1:
        #                     res += s(mask_p[:p] + \"0\" + mask_p[p+1:], h-1, n-1)
        #                 else:
        #                     res += 1
        #     cache[c] = res%const
        #     return cache[c]
        # mask_p = \"1\"*len(hats)
        # return s(mask_p, maxx, len(hats))%const


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        

    def _to_hat_to_people(self, person_to_hats):
        min_hat, max_hat = None, None
        for hats in person_to_hats:
            for hat in hats:
                if min_hat is None or hat < min_hat:
                    min_hat = hat
                if max_hat is None or hat > max_hat:
                    max_hat = hat

        number_of_hats = max_hat - min_hat + 1

        hats_to_people = [[] for _ in range(number_of_hats)]
        for person in range(len(person_to_hats)):
            for hat in person_to_hats[person]:
                hats_to_people[hat - min_hat].append(person)
        return hats_to_people

    def _number_of_ways(self, hat_to_people, person_to_hat_presence, hat, cache):
        if all(person_to_hat_presence):
            return 1
        if hat >= len(hat_to_people):
            return 0
        key = hat, tuple(person_to_hat_presence)
        if key in cache:
            return cache[key]
        else:
            sum = 0
            for person in hat_to_people[hat]:
                if not person_to_hat_presence[person]:
                    updated_person_to_hat_presence = person_to_hat_presence.copy()
                    updated_person_to_hat_presence[person] = True
                    sum += self._number_of_ways(hat_to_people, updated_person_to_hat_presence, hat + 1, cache)
            sum += self._number_of_ways(hat_to_people, person_to_hat_presence, hat + 1, cache)
            cache[key] = sum%(10**9+7)
            return cache[key]

    def numberWays(self, person_to_hats):
        hat_to_people = self._to_hat_to_people(person_to_hats)
        return self._number_of_ways(hat_to_people, [False] * len(person_to_hats), 0, {})
