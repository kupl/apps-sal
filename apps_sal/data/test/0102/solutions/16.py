s = int(input())


def slovo1(x):
    if x == 0:
        return 'zero'
    if x == 1:
        return 'one'
    if x == 2:
        return 'two'
    if x == 3:
        return 'three'
    if x == 4:
        return 'four'
    if x == 5:
        return 'five'
    if x == 6:
        return 'six'
    if x == 7:
        return 'seven'
    if x == 8:
        return 'eight'
    if x == 9:
        return 'nine'


def slovo2(x):
    if x == 10:
        return 'ten'
    if x == 11:
        return 'eleven'
    if x == 12:
        return 'twelve'
    if x == 13:
        return 'thirteen'
    if x == 14:
        return 'fourteen'
    if x == 15:
        return 'fifteen'
    if x == 16:
        return 'sixteen'
    if x == 17:
        return 'seventeen'
    if x == 18:
        return 'eighteen'
    if x == 19:
        return 'nineteen'


def slovo3(x):
    if x == 20:
        return 'twenty'
    if x == 30:
        return 'thirty'
    if x == 40:
        return 'forty'
    if x == 50:
        return 'fifty'
    if x == 60:
        return 'sixty'
    if x == 70:
        return 'seventy'
    if x == 80:
        return 'eighty'
    if x == 90:
        return 'ninety'


if s < 10:
    print(slovo1(s))
elif s >= 10 and s < 20:
    print(slovo2(s))
elif s % 10 == 0:
    print(slovo3(s))
else:
    k = str(slovo3(s // 10 * 10)) + '-' + str(slovo1(s % 10))
    print(k)
