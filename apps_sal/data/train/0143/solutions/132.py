class Solution:
    def totalFruit(self, f: List[int]) -> int:
        start, count, maxFruits = 0, 0, 0
        fruitHash = defaultdict(int)

        for end in range(len(f)):
            if fruitHash[f[end]] == 0:
                count += 1
            fruitHash[f[end]] += 1

            if count <= 2:
                maxFruits = max(maxFruits, end - start + 1)

            while count > 2:
                fruitHash[f[start]] -= 1
                start += 1
                if fruitHash[f[start - 1]] == 0:
                    count -= 1
                    maxFruits = max(maxFruits, end - start + 1)
        return maxFruits
