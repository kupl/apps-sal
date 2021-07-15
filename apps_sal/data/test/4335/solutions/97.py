N = int(input())
S = input()
if N % 2 != 0:
    print('No')
else:
    for i in range(int(N/2)):
        if S[i] != S[i + int(N/2)]:
            print('No')
            break
    else:
        print('Yes')
