def main():
    q = int(input())
    thirds = [1]
    while thirds[-1] < 1e19:
        thirds.append(thirds[-1] * 3)
    for t in range(q):
        a = int(input())
        deg = 0
        subans = 0
        while subans < a:
            subans += thirds[deg]
            deg += 1
        while deg != -1:
            if subans - thirds[deg] >= a:
                subans -= thirds[deg]
            deg -= 1
        print(subans)


main()
