class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = len(dominoes)
        right_force = [0]*l
        left_force = [0]*l
        force1 = 0
        force2 = 0
        for i in range(l):
            if dominoes[i]=='R':
                force1 = l
            elif dominoes[i]=='L':
                force1 = 0
            else:
                force1 = max(force1 - 1, 0)
            right_force[i] += force1
        for i in range(l-1, -1, -1):
            if dominoes[i]=='L':
                force2 = l
            elif dominoes[i]=='R':
                force2 = 0
            else:
                force2 = max(force2 - 1, 0)
            left_force[i] += force2

        result = ''
        for i in range(l):
            if right_force[i] > left_force[i]:
                result += 'R'
            elif right_force[i] < left_force[i]:
                result += 'L'
            else:
                result += '.'
        return result
