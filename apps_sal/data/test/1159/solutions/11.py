def make_prime_table(n):
    '''n以下の非負整数が素数であるかを判定するためのリストを出力する
    計算量: O(NloglogN)
    入出力例: 6 -> [False, False, True, True, False, True, False]'''
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False
    return is_prime


li = make_prime_table(10000)
n = int(input())
ans = []
for i in range(n-1):
    ans.append((i+1, i+2))
ans.append((i+2, 1))

s = 0
t = n - 2
while not li[len(ans)]:
    ans.append((s+1, t+1))
    s += 1
    t -= 1
print(len(ans))
for i in range(len(ans)):
    print(" ".join(map(str, ans[i])))



