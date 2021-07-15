import copy

N, K = list(map(int, input().split()))
my_R, my_S, my_P = list(map(int, input().split()))
hand_score = {'r': my_P, 's': my_R, 'p': my_S}
T = input()
ans = 0

for i in range(K):
    cnt = (N - i - 1) // K + 1
    dp = {'R': 0, 'S': 0, 'P': 0}
    new_dp = {'R': 0, 'S': 0, 'P': 0}
    for j in range(cnt):
        check = {'r': 0, 's': 0, 'p': 0}
        check[T[(j * K) + i]] = hand_score[T[(j * K) + i]]

        new_dp['R'] = max(dp['S'] + check['s'], dp['P'] + check['p'])
        new_dp['S'] = max(dp['P'] + check['p'], dp['R'] + check['r'])
        new_dp['P'] = max(dp['R'] + check['r'], dp['S'] + check['s'])

        dp = copy.copy(new_dp)
    ans += max(dp.values())
print(ans)

