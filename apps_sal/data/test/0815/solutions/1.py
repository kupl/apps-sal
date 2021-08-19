(v1, v2, v3, v4) = list(map(int, input().split()))


def main():
    for i in range(v3, 2 * v3 + 1):
        if 2 * v4 >= i >= v4:
            for j in range(max(i + 1, v2), 2 * v2 + 1):
                if 2 * v4 < j:
                    for k in range(max(j + 1, v1), 2 * v1 + 1):
                        return (i, j, k)


ans = main()
if ans:
    print(ans[2], ans[1], ans[0], sep='\n')
else:
    print(-1)
