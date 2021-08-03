# I'm feeling greedy
base = int(input())
num = input()

result = 0
place_value = 1
end = len(num)
while end > 0:
    begin = end - 1
    good_begin = begin
    while begin >= 0:
        if int(num[begin:end]) >= base:
            break
        elif num[begin] != '0':
            good_begin = begin
        begin -= 1
    begin = good_begin
    result += place_value * int(num[begin:end])
    place_value *= base
    end = begin

print(result)
