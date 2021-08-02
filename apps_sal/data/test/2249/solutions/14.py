

def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    seen = set()
    count = 0
    distinct = [0]
    for x in reversed(a):
        if x in seen:
            distinct.append(distinct[-1])
            continue
        seen.add(x)
        distinct.append(distinct[-1] + 1)
    distinct.pop()
    seen.clear()
    # print(tuple(reversed(distinct)))
    for x, distinct_right in zip(a, reversed(distinct)):
        #print(x, distinct_right)
        if x in seen:
            continue
        seen.add(x)
        count += distinct_right

    print(count)


main()
