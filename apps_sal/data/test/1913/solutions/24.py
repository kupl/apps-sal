input()
numbers = input().split()


def is_non_beautiful(x):
    cnt_one = 0
    for c in x:
        if c != '0' and c != '1':
            return True
        if c == '1':
            cnt_one += 1
        if cnt_one > 1:
            return True
    return False


non_beautiful = ""
zero_count = 0
for x in numbers:
    if len(x) == 1 and int(x) == 0:
        print(0)
        return
    if is_non_beautiful(x):
        non_beautiful = x
    else:
        zero_count += x.count("0")

if non_beautiful == "":
    print("1" + "0" * zero_count)
else:
    print(non_beautiful + "0" * zero_count)
