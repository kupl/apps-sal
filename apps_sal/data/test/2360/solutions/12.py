def solve(students):
    k = 1
    for s in students:
        if s[1] < k:
            print(0, end=' ')
        else:
            print(max(s[0], k), end=' ')
            if k < s[0]:
                k = s[0] + 1
            else:
                k += 1
    print()


tests = int(input())
while tests:
    tests -= 1
    n = int(input())
    st = []
    for _ in range(n):
        st.append(list(map(int, input().split())))
    solve(st)
