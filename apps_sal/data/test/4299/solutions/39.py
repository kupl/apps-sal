N = int(input())

tem = N%10

hon = [2,4,5,7,9]
pon = [0,1,6,8]
bon = [3]

if tem in hon:
    print("hon")
elif tem in pon:
    print("pon")
elif tem in bon:
    print("bon")
