def main():
    s = input()
    n = len(s)
    nums = [[], [], []]
    if n == 1:
        print(s)
        return 0
    for i in range(n):
        nums[int(s[i])].append(i)
    if len(nums[0]) == 0:
        temp = len(nums[1])
        print('1' * temp + '2' * (n - temp))
    elif len(nums[2]) == 0:
        temp = len(nums[0])
        print('0' * temp + '1' * (n - temp))
    else:
        S = [i for i in s if i != '1']
        temp = len(nums[1])
        for i in range(len(S)):
            if S[i] == '2':
                break
        print(''.join(S[:i]) + temp * '1' + ''.join(S[i:]))
    return 0


main()
