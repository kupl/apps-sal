#!/usr/bin/env python3

def main():
	a = str(input())
	if a[-1] == 's':
		print((a + 'es'))
	else:
		print((a + 's'))


def __starting_point():
	main()

__starting_point()
