# cook your dish here
try:
    def socks():
        jacket, sock, money = map(int, input().split())
        rem = money - jacket
        a = rem // sock
        if(a % 2 == 0):
            print("Lucky Chef")
        else:
            print("Unlucky Chef")
    socks()
except:
    pass
