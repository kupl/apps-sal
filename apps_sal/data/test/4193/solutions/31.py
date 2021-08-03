def main():
    A = []
    C = [False] * 9
    for i in range(3):
        a0, a1, a2 = map(int, input().split())
        A.append(a0)
        A.append(a1)
        A.append(a2)

    N = int(input())
    for i in range(N):
        b = int(input())
        if b in A:
            C[A.index(b)] = True

    for i in range(3):
        if C[0 + 3 * i] and C[1 + 3 * i] and C[2 + 3 * i]:
            print("Yes")
            return

    for i in range(3):
        if C[i] and C[i + 3] and C[i + 6]:
            print("Yes")
            return

    if C[0] and C[4] and C[8]:
        print("Yes")
        return

    if C[2] and C[4] and C[6]:
        print("Yes")
        return

    print("No")


main()
