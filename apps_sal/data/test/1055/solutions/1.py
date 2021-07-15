def helper(arr):
    if arr == sorted(arr): return len(arr)
    return max(helper(arr[:len(arr) // 2]), helper(arr[len(arr) // 2:]))

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(helper(arr))
    return 0

main()
