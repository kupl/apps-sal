def __starting_point():

    q = int(input())

    for t in range(q):
        n = int(input())
        l = [int(i) for i in input().split(" ")]

        flag = True
        ans = []

        for i in range(1, len(l) + 1):
            j = l[i - 1]
            count = 1

            while j != i:
                j = l[j-1]
                count += 1
            ans.append(count)

        for i in ans:
            print(i, end=' ')
        print()

__starting_point()
