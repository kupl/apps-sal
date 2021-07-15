# bit全探索
n = int(input())
# 各人における別の人への証言
q = [["-"] * n for _ in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        q[i][x - 1] = False if y == 0 else True
ans = 0
for bit in range(1 << n):
    arr = [False] * n
    for i in range(n):
        if bit >> i & 1 == 1:
            arr[i] = True
    flag = True
    for i in range(n):
        if arr[i] == False:
            # 不親切の人のいうことは聞く必要ない
            continue
        # 人iは正直者だと仮定して探索
        for j in range(n):
            if q[i][j] == "-":
                # そもそも言及してない
                continue
            if q[i][j] != arr[j]:
                # 仮定がくずれた
                flag = False
                break
    if flag:
        ans = max(ans, arr.count(True))
print(ans)
