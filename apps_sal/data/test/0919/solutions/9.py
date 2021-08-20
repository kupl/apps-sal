(n, k) = list(map(int, input().split()))
s = input()
has = [ord(el) - 96 for el in sorted(s)]
ans = has[0]
last = ans
done = 1
i = 1
while i < n and done < k:
    if has[i] - 2 >= last:
        ans += has[i]
        last = has[i]
        done += 1
    i += 1
if done == k:
    print(ans)
else:
    print(-1)
