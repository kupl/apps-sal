class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0] * k
        for num in arr:
            count[num % k] += 1

        # Now since we have 0,1,2,.....k-1 as residues
        # If count[1] == count[k-1],pairs+=count[0]
        print(count)
        for x in range(k):
            comp = -x % k
            # x+comp = 0 mod k, or
            # (x+comp) mod k = 0
            print(comp)
            while count[x] > 0:
                count[x] -= 1
                count[comp] -= 1
                if count[comp] < 0:
                    return False

        return True
