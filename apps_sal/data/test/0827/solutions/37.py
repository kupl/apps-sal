N = int(input())
S = input()

if N == 1:
    if S == '0':
        print(10**10)
    else:
        print(2 * 10**10)

else:
    if S[:2] == '11':
        for i in range(N):
            if i % 3 == 2 and S[i] == '1':
                print(0)
                break
            if i % 3 != 2 and S[i] == '0':
                print(0)
                break
        else:
            print((3 * 10**10 - N) // 3 + 1)
            
    elif S[:2] == '10':
        for i in range(N):
            if i % 3 == 1 and S[i] == '1':
                print(0)
                break
            if i % 3 != 1 and S[i] == '0':
                print(0)
                break
        else:
            print((3 * 10**10 - N - 1) // 3 + 1)
            
    elif S[:2] == '01':
        for i in range(N):
            if i % 3 == 0 and S[i] == '1':
                print(0)
                break
            if i % 3 != 0 and S[i] == '0':
                print(0)
                break
        else:
            print((3 * 10**10 - N - 2) // 3 + 1)
            
    else:
        print(0)
