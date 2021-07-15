K = int(input())

def calc_sunuke(num):
    st = str(num)
    s_num = 0
    for c in st:
        s_num += int(c)
    return num / s_num

def search_sunuke(num):
    num_sunuke = calc_sunuke(num)
    if num >= 100:
        digits = len(str(num))
        if digits < 12:
            for i in range(count + 10**(digits-2), 10**digits, 10**(digits-2)):
                if num_sunuke > calc_sunuke(i):
                    return False
            return True
        else:
            for i in range(count + 10**(digits-3), 10**digits, 10**(digits-3)):
                if num_sunuke > calc_sunuke(i):
                    return False
            return True
    else:
        for i in range(count+1, 100):
            if num_sunuke > calc_sunuke(i):
                return False
        return True



count = 1
sunuke_num = 0
while sunuke_num != K:
    if search_sunuke(count):
        print(count)
        sunuke_num += 1
    if count < 99:
        count += 1
    else:
        count_str = str(count)
        digits = len(count_str)
        r_count = count
        if digits < 12:
            for c in count_str:
                if c != '9':
                    count += 10**(digits - 2)
                    break
            if r_count == count:
                count += 10**(digits - 1)
        else:
            for c in count_str:
                if c != '9':
                    count += 10**(digits - 3)
                    break
            if r_count == count:
                count += 10**(digits - 2)
        


