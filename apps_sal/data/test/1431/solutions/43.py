N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] * (N + 1)  # ボールの管理

# 大きい数字から1まで順に見ていく
for i in reversed(range(1, N + 1)):
    ball = 0
    base = i + 1

    # iからNまでiずつ見てボールを足す(j=iの倍数)
    for j in range(i, N + 1, i):
        ball += B[j]

    # もし足したボールの数%2がA[i]と合わないなら合わせる
    if ball % 2 != A[i]:
        B[i] = 1

print(sum(B))  # ボールの入った箱の総数
# もしBに1が入っている場所があればその場所を出力
print(*[i for i, b in enumerate(B) if b == 1], sep=' ')
