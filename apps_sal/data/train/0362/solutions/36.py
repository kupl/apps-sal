class Solution:

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
            cache[key] = sum % (10**9 + 7)
            return cache[key]

    def numberWays(self, person_to_hats):
        hat_to_people = self._to_hat_to_people(person_to_hats)
        return self._number_of_ways(hat_to_people, [False] * len(person_to_hats), 0, {})
