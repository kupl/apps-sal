# Original Submission At: https://atcoder.jp/contests/abc149/submissions/16823042
x= int(input())

def prime_check(num,count):
    while True:
        while num % count == 0:
            num = num + 1
            count = 2
        if num <= count**2:
            print(num)
            break
        else:
            count = count + 1

if x==2 :
    print((2))
else:
    prime_check(x,2)

