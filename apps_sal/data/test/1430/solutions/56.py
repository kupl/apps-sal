N, K = map(int, input().split())
S = input().rstrip('\n')

S += '1' if S[N - 1] == '0' else '0'
sumz = [0] * (N + 2)
right = 1
cnt = 1
maxlen = 0
left = 0
if K == 0:
    for i in range(N):
        if S[i] == S[i + 1] and S[i] == 1:
            cnt += 1
        else:
            if maxlen < cnt:
                maxlen = cnt
            cnt = 1
else:
    cnt = 0
    while True:
        if left >= N:
            break
        if right <= left:
            right = left + 1
        while (right < N) and ((cnt < K) or ((cnt == K) and ((S[right] == S[right - 1]) or S[right] == '1'))):
            if (S[right] != S[right - 1]) and (S[right - 1] == '0'):
                cnt += 1
            right += 1

        if not(S[right - 1] == '0' and (K == 0)):
            if maxlen < right - left:
                maxlen = right - left
        while left < N and S[left] == S[left + 1]:
            left += 1
        if S[left] == '0':
            cnt -= 1

        left += 1

print(maxlen)
