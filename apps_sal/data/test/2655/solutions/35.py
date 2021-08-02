def chat_in_a_circle():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    res = A.pop(-1)
    t = len(A) % 2 == 0
    a = 0
    for i in range(len(A) // 2):
        a = A.pop(-1)
        res += a * 2
    if t:
        res -= a

    print(res)


chat_in_a_circle()
