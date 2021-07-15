for _ in range(int(input())):
    x = int(input())
    s = input()
    if 'R' in s and "L" in s:
        A = []
        if s[0] == 'R':
            A.append([1, 1])
        else:
            A.append([2, 1])
        for i in range(1, len(s)):
            if A[-1][0] == 1:
                if s[i] == 'R':
                    A[-1][1] += 1
                else:
                    A.append([2, 1])
            else:
                if s[i] == 'L':
                    A[-1][1] += 1
                else:
                    A.append([1, 1])
        if A[0][0] == A[-1][0]:
            A[0][1] += A[-1][1]
            A.pop()
        Ans = 0
        for i in range(len(A)):
            Ans += A[i][1] // 3
        print(Ans)
    else:
        print((len(s) + 2) // 3)
