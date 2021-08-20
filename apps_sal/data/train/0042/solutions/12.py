for _ in range(int(input())):
    s = input()
    num_zero = 0
    ans = 0
    length = len(s)
    for i in range(length):
        if s[i] == '0':
            num_zero += 1
        else:
            act_num = 1
            j = i
            is_right = True
            while j < length and is_right:
                if act_num - (j - i + 1) <= num_zero:
                    ans += 1
                    j += 1
                    if j < length:
                        act_num = act_num * 2 + int(s[j])
                else:
                    is_right = False
            num_zero = 0
    print(ans)
