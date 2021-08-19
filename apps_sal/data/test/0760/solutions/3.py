s = input().rstrip()
k = int(input())
if k > len(s):
    print(len(s) + k - ((len(s) + k) % 2 == 1))
else:
    aux = []
    for j in range(1, len(s)):
        i = len(s) - 1
        cnt = 0
        while i - j >= 0 and s[i] == s[i - j]:
            i -= 1
            cnt += 1
            if cnt == j:
                break
        diff = i - (len(s) - j - 1)
        if diff <= k:
            aux.append(2 * j)
    aux.append(2 * k)
    for i in range(len(s)):
        for j in range((len(s) - i) // 2):
            if s[i:i + j] == s[i + j:i + 2 * j]:
                aux.append(2 * j)
    print(max(aux))
