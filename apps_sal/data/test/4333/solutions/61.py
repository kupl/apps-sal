x1, y1, x2, y2 = map(int, input().split())
x_len = x2 - x1
y_len =  y2 - y1
print("{} {} {} {}".format(x2-y_len,y2+x_len,x1-y_len,y1+x_len))
