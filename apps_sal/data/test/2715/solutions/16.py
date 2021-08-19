K = int(input())
ans = [49 + K // 50] * 50
amari = K % 50
if amari != 50:
    for i in range(amari):
        ans[i] = ans[i] + 50 - (amari - 1)
    for i in range(amari, 50):
        ans[i] = ans[i] - amari
print(50)
ansstr = [str(i) for i in ans]
print(' '.join(ansstr))
