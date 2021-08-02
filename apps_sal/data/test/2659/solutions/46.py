import math
# import datetime


def s(n):
    sum = 0
    for c in str(n):
        sum += int(c)
    return sum


k = int(input())
found = 0


def next_sunuke(n, s_n, s_n_div):

    nonlocal found

    if n == 1:
        return

    log_n = int(math.log(n, 10))
    m = n - 10 ** int(log_n // 1.25)
    # m = n - 1

    while m >= 1:
        s_m = s(m)
        s_mplus1 = s(m + 1)

        # if (s_m < s_mplus1 or (s_n - s_m != 1 and s_n - s_m != -8)) and m > 9:
        if (s_m < s_mplus1) and m > 9:
            m -= 10 ** int(log_n // 1.25)
            continue

        # print("check: " + str(m))

        s_m_div = m / s(m)

        if s_m_div <= s_n_div:
            next_sunuke(m, s_m, s_m_div)
            if found >= k:
                return

            found += 1
            # print("{0:d}".format(m), "{0:+d}".format(n-m), "{0:d}".format(s_m), s_m_div)
            print(m)
            break
        # else:
        # 	log_m = int(math.log(m,10))
        # 	if (m + 1) / (10 ** (log_m - 1)) == 19:

        # 		print ("skip: " + str(m) + " to " + str(10 ** log_m - 1))

        # 		m = 10 ** log_m - 1
        # 		s_mplus1 = s(m+1)
        # 		continue

        m -= 10 ** int(log_n // 1.25)


# 適当な大きいスヌケ数
current_sunuke = 999999999999999
s_current_sunuke = s(current_sunuke)
s_current_sunuke_div = current_sunuke / s_current_sunuke

# start = datetime.datetime.now()
next_sunuke(current_sunuke, s_current_sunuke, s_current_sunuke_div)
if found < k:
    print(current_sunuke)
# end = datetime.datetime.now()
# print(str(end-start))

# sunukes=[]

# n = current_sunuke - 1

# while(n >= 1):
# 	s_n = n / s(n)
# 	if s_n <= current_sunuke_n:
# 		#sunukes.insert(0,n)
# 		sunukes.append(n)
# 		current_sunuke = n
# 		current_sunuke_n = s_n
# 	n -= 1

# for n in sunukes:
# 	print (n)
