class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        alive = set()
        dead = set()
        for num1 in A:
            tmp = {num1}
            for num2 in alive:
                dead.add(num2)
                tmp.add(num1|num2)
            alive = tmp
            
        return len(alive|dead)
