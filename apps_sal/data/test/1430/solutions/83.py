N, K = list(map(int, input().split()))
S = input()
left = 0
right = 0
numofturn = 0
if N == 1:
    print((int(S)))
else:
    if S[0] == "0":
        while(right < N):
            if S[right] == "0":
                right += 1
            else:
                break
    # print(right)
    right = max(right, 1)
    while(right < N and numofturn < K):
        if S[right] == "1" and S[right - 1] == "0":
            numofturn += 1
        right += 1
    while(right < N):
        if S[right] == "1":
            right += 1
        else:
            break
    # print(right)
    ans = right
    while(right < N and left < N):
        if numofturn == K:
            while(1):
                left += 1
                if left < N:
                    if S[left] != "1" or S[left - 1] != "0":
                        continue
                numofturn -= 1
                break
        else:
            while(1):
                right += 1
                if right < N:
                    if S[right] != "0" or S[right - 1] != "1":
                        continue
                numofturn += 1
                if right == N:
                    ans = max(ans, right - left)
                else:
                    ans = max(ans, right - left)
                # print(ans,left,right)
                break
    print(ans)
    # print(left,right)
