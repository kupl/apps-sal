P, Q, R = map(int,input().split())

Flight_time = [P+Q, Q+R, R+P]

print(min(Flight_time))
