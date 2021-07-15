def main():
    m = int(input())

    for i in range(m):
        n = int(input())
        nums = map(int, input().split())
        arr = {}
        for j in nums:
            base = j
            step = 0
            while not base & 1:
                base >>= 1
                step += 1

            if not base in arr:
                arr[base] = step
            else:
                arr[base] = max(arr[base], step)

        print(sum(arr.values()))



def __starting_point():
    main()
__starting_point()
