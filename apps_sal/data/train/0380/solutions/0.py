class Solution:

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if ':' in IP:
            res = self.validIPv6(IP)
            return 'IPv6' if res else 'Neither'
        elif '.' in IP:
            res = self.validIPV4(IP)
            return 'IPv4' if res else 'Neither'
        else:
            return 'Neither'

    def validIPV4(self, IP):
        charSet = set(list('0123456789'))
        parts = IP.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if len(part) < 1:
                return False
            for c in part:
                if c not in charSet:
                    return False
            if not 0 <= int(part) <= 255:
                return False
            if part[0] == '0' and len(part) > 1:
                return False
        return True

    def validIPv6(self, IP):
        charSet = set(list('0123456789abcdefABCDEF'))
        parts = IP.split(':')
        if len(parts) != 8:
            return False
        zeroFlag = False
        omtFlag = False
        for part in parts:
            if len(part) == 0:
                omtFlag = True
            if self.allZero(part):
                zeroFlag = True
            if len(part) > 4:
                return False
            for c in part:
                if c not in charSet:
                    return False
        if zeroFlag and omtFlag:
            return False
        return True

    def allZero(self, s):
        for i in range(len(s)):
            if s[i] != '0':
                return False
        return True
