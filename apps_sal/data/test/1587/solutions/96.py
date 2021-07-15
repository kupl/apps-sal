n = int(input())
c = input()

r_cnt = c.count("R")

print(r_cnt - c[:r_cnt].count("R"))
