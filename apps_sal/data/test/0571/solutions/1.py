def main():
    n = int(input())
    arr = list(input())
    if n & 1:
        print(":(")
        return 0
    left = n // 2 - arr.count('(')
    for i in range(n):
        if arr[i] == '?':
            if left:
                arr[i] = '('
                left -= 1
            else:
                arr[i] = ')'
    if arr[0] == ')' or arr[-1] == '(':
        print(":(")
        return 0
    left = 1
    right = 0
    for i in range(1, n):
        if right == left:
            print(":(")
            return 0
        if arr[i] == '(':
            left += 1
        else:
            right += 1
    if left != right:
        print(":(")
        return 0
    print("".join(arr))
    return 0


main()
