h,w = map(int,input().split())

if h % 3 == 0 or w % 3 == 0:
    print(0)
else:
    best = (h*w)/3
    # wから割る方法
    col_num = int(round(best/h))
    remain_w = w - col_num
    h1 = h // 2
    h2 = h - h1
    w1 = remain_w // 2
    w2 = remain_w - w1
    min_area1 = min(remain_w*h1, remain_w*h2, col_num*h) # 垂直
    max_area1 = max(remain_w*h1, remain_w*h2, col_num*h)
    min_area2 = min(w2*h, w1*h, col_num*h) # 平行
    max_area2 = max(w2*h, w1*h, col_num*h)
    num_w1 = max_area1 - min_area1
    num_w2 = max_area2 - min_area2
    # hから割る方法
    row_num = int(round(best/w))
    remain_h = h - row_num
    w1 = w // 2
    w2 = w - w1
    h1 = remain_h // 2
    h2 = remain_h - h1
    min_area1 = min(remain_h*w1, remain_h*w2, row_num*w) # 垂直
    max_area1 = max(remain_h*w1, remain_h*w2, row_num*w)
    min_area2 = min(h2*w, h1*w, row_num*w) # 平行   
    max_area2 = max(h2*w, h1*w, row_num*w)
    num_h1 = max_area1 - min_area1
    num_h2 = max_area2 - min_area2
    print(min(num_h1,num_w1,num_h2,num_w2))
