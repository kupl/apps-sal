s = input()
num = len(s)

tar_index = len(s) - 1
count = 0

while (count < num):
    tar = s[:tar_index]
    tar_num = len(tar)
    # 文字数が奇数の時は、偶文字列にはならない。
    if (tar_num % 2 == 0):
        half = int(tar_num / 2)

        if (tar[:half] == tar[half:]):
            print((int(2 * len(tar[:half]))))
            return
        else:
            pass

    else:
        pass

    tar_index -= 1
    count += 1

