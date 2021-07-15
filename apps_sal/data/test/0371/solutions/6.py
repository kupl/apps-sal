cubes = [i**3.0 for i in range(2, int(1.8e5+5))]

def valid(mid):
    return sum([mid//i for i in cubes if i <= mid])

def binary_search(k):
    l = int(4.8 * k)
    r = min(8.0 * k, 5.0 * (10**15))
    while (l+1 < r):
        mid = (l+r) / 2.0
        res = valid(mid)
        if (res < k):
            l = mid
        else:
            r = mid
    return int(r) if int(valid(r)) == k else -1

def main():
    k = int(input())
    print(binary_search(k))

main()

