(n, k) = list(map(int, input().split()))
arr = list(map(int, input().split()))
s = str(input())
i = 0
ans = 0
while i < n:
    j = i + 1
    count = 1
    arrx = [arr[i]]
    while j < n and s[i] == s[j]:
        count += 1
        arrx.append(arr[j])
        j += 1
    arrx.sort(reverse=True)
    ans += sum(arrx[:min(count, k)])
    i = j
print(ans)
