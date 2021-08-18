class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        forces = [0] * len(dominoes)
        max_force = len(dominoes)

        force = 0
        for i, d in enumerate(dominoes):
            if d == 'R':
                force = max_force
            elif d == 'L':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] += force

        force = 0
        for i in range(len(dominoes) - 1, -1, -1):
            d = dominoes[i]
            if d == 'L':
                force = max_force
            elif d == 'R':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force

        print(forces)

        result = ''
        for f in forces:
            if f == 0:
                result += '.'
            elif f > 0:
                result += 'R'
            else:
                result += 'L'
        return result
