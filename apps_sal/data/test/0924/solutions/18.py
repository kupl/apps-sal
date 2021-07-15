import math

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)


(la, ra, ta) = [int(s) for s in input().split(" ")]
(lb, rb, tb) = [int(s) for s in input().split(" ")]

delta = gcd(ta, tb)
# print(delta)

def overlap(al, ar, bl, br):
    return max(0, min(ar, br) - max(al, bl) + 1)

def eval(fst_, snd_):
    result_ = 0

    k1 = math.ceil(abs(fst_[0] - snd_[0])/delta)
    k2 = abs(fst_[0] - snd_[0]) // delta

    for k in (k1, k2):
        pos_sndl = snd_[0]
        pos_sndr = snd_[1]
        pos_fstl = k * delta + fst_[0]
        pos_fstr = k * delta + fst_[1]
        intersection = overlap(pos_sndl, pos_sndr, pos_fstl, pos_fstr)
        # print(intersection)
        # print(pos_sndl, pos_sndr, pos_fstl, pos_fstr, intersection)
        result_ = max(result_, intersection)


    # pos_sndl = snd_[0]
    # pos_sndr = snd_[1]
    # pos_fstl = fst_[0]
    # pos_fstr = fst_[1]
    # intersection = overlap(pos_sndl, pos_sndr, pos_fstl, pos_fstr)
    # result_ = max(result_, intersection)
    # # print(delta)
    # # print(intersection)
    # snd_k = (snd_[1] - fst_[0]) // delta + 1
    # fst_k = (snd_[0] - fst_[1]) // delta -1
    #
    # print(fst_k, snd_k)
    #
    # for k in range(fst_k, snd_k):
    #     pos_sndl = snd_[0]
    #     pos_sndr = snd_[1]
    #     pos_fstl = k * delta + fst_[0]
    #     pos_fstr = k * delta + fst_[1]
    #     intersection = overlap(pos_sndl, pos_sndr, pos_fstl, pos_fstr)
    #     # print(intersection)
    #     # print(pos_sndl, pos_sndr, pos_fstl, pos_fstr, intersection)
    #     result_ = max(result_, intersection)

    return result_


fst_ = (la, ra, ta)
snd_ = (lb, rb, tb)

result = max(eval(fst_, snd_), eval(snd_, fst_))
print(result)
