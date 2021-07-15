#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
from collections import Counter


def main():
	n = int(input())
	cnt = Counter(map(int, input().split()))
	for a, val in cnt.items():
		if val % 2 == 1:
			print("Conan")
			return
	print("Agasa")

def __starting_point():
	main()
__starting_point()
