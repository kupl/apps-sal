import math
N, A, B = list(map(int, input().split()))
all_attack = 0
enemy = [int(input()) for i in range(N)]


def possible_kill_all(attack):
    tmp_enemy = [v - B * attack for v in enemy]
    tmp_needed_attack = 0
    for v in tmp_enemy:
        if v > 0:
            tmp_needed_attack += math.ceil(v / (A - B))
    if tmp_needed_attack <= attack:
        return True
    else:
        return False


possible = 10**14
impossible = 0

while possible - impossible > 1:
    M = (possible + impossible) // 2
    if possible_kill_all(M):
        possible = M
    else:
        impossible = M

print(possible)
