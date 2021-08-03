def solve1(a, n):
    left = []
    st = []
    i = 0
    while i < (n):
        if not st:
            left.append(-1)
            st.append(i)

        elif st and a[i] < a[st[-1]]:
            left.append(st[-1])
            st.append(i)
        else:
            while st and a[i] > a[st[-1]]:
                st.pop()

            if not st:
                st.append(i)
                left.append(-1)

            else:
                left.append(st[-1])
                st.append(i)

        i += 1
    # print(left)
    right = []
    st = []
    i = n - 1
    while i > (-1):
        if not st:
            right.append(n)
            st.append(i)

        elif st and a[i] < a[st[-1]]:
            right.append(st[-1])
            st.append(i)
        else:
            while st and a[i] >= a[st[-1]]:
                st.pop()

            if not st:
                st.append(i)
                right.append(n)

            else:
                right.append(st[-1])
                st.append(i)

        i -= 1
    right = right[::-1]
    c = 0
    for i in range(len(left)):
        x = (right[i] - i) * (i - left[i]) * a[i]
        # print(x)
        if x == 0:
            c += a[i]
        else:
            c += x
    # print(c)
    # print(a)
    # print(left)
    # print(right)

    return c


def solve2(a, n):
    left = []
    st = []
    i = 0
    while i < (n):
        if not st:
            left.append(-1)
            st.append(i)

        elif st and a[i] > a[st[-1]]:
            left.append(st[-1])
            st.append(i)
        else:
            while st and a[i] < a[st[-1]]:
                st.pop()

            if not st:
                st.append(i)
                left.append(-1)

            else:
                left.append(st[-1])
                st.append(i)

        i += 1
    # print(left)
    right = []
    st = []
    i = n - 1
    while i > (-1):
        if not st:
            right.append(n)
            st.append(i)

        elif st and a[i] > a[st[-1]]:
            right.append(st[-1])
            st.append(i)
        else:
            while st and a[i] <= a[st[-1]]:
                st.pop()

            if not st:
                st.append(i)
                right.append(n)

            else:
                right.append(st[-1])
                st.append(i)

        i -= 1
    right = right[::-1]
    # print(right)
    c = 0
    for i in range(len(left)):
        x = (right[i] - i) * (i - left[i]) * a[i]
        # print(x)
        if x == 0:
            c += a[i]
        else:
            c += x
    # print(c)
    # print(a)
    # print(left)
    # print(right)

    return c


n = int(input())
arr = [int(x) for x in input().split()]
# solve2(arr,n)
# print(solve1(arr,n))
# print(solve2(arr,n))
# print()
# (solve2(arr,n))

print(solve1(arr, n) - solve2(arr, n))
