# 1.　s1,s2,s3を入力する
s1, s2, s3 = list(map(str,input().split()))

# 2.　s1,s2,s3の先頭文字を取り出して、一つのリストに格納する
s_list = [s1[0], s2[0], s3[0]]

# 3.　2を結合し、大文字にする
s = "".join(s_list)
ss = s.upper()

# 4.　3を大文字にする
print(ss)

