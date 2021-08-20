from math import gcd
from collections import defaultdict
from sys import stdin, stdout


def main():
    GCD_count = defaultdict(int)
    GCD_map = defaultdict(int)
    arr_len = int(stdin.readline())
    arr = [int(x) for x in stdin.readline().split()]
    for start in range(arr_len):
        temp = defaultdict(int)
        GCD_count[arr[start]] += 1
        temp[arr[start]] += 1
        for (gcd_now, occurence) in list(GCD_map.items()):
            res = gcd(gcd_now, arr[start])
            temp[res] += occurence
            GCD_count[res] += occurence
        GCD_map = temp
    num_queries = int(stdin.readline())
    for _ in range(num_queries):
        print(GCD_count[int(stdin.readline())])


main()
